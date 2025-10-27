
import cv2
import numpy as np
import matplotlib.pyplot as plt

# ========== EDGE-BASED SEGMENTATION ==========
def sobel_edge_detection(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    sobel_mag = np.sqrt(sobel_x ** 2 + sobel_y ** 2)
    sobel_mag = np.uint8(sobel_mag / sobel_mag.max() * 255)

    plt.figure(figsize=(12,4))
    plt.subplot(1,3,1), plt.imshow(sobel_x, cmap='gray'), plt.title('Sobel X')
    plt.subplot(1,3,2), plt.imshow(sobel_y, cmap='gray'), plt.title('Sobel Y')
    plt.subplot(1,3,3), plt.imshow(sobel_mag, cmap='gray'), plt.title('Magnitude')
    plt.show()
    return sobel_mag

def canny_edge_detection(image_path, low=100, high=200):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    edges = cv2.Canny(image, low, high)
    plt.imshow(edges, cmap='gray')
    plt.title('Canny Edge Detection')
    plt.axis('off')
    plt.show()
    return edges

# ========== REGION-BASED SEGMENTATION ==========
def region_growing(image, seed, threshold=10):
    visited = np.zeros_like(image)
    region = []
    queue = [seed]

    while queue:
        x, y = queue.pop(0)
        if visited[x, y] == 0:
            if abs(int(image[x, y]) - int(image[seed])) < threshold:
                region.append((x, y))
                visited[x, y] = 1
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < image.shape[0] and 0 <= ny < image.shape[1]:
                        queue.append((nx, ny))
    return visited

def watershed_segmentation(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    ret, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    kernel = np.ones((3,3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
    sure_bg = cv2.dilate(opening, kernel, iterations=3)
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)
    ret, markers = cv2.connectedComponents(sure_fg)
    markers = markers + 1
    markers[unknown == 255] = 0
    markers = cv2.watershed(color, markers)
    color[markers == -1] = [255, 0, 0]
    plt.imshow(cv2.cvtColor(color, cv2.COLOR_BGR2RGB))
    plt.title('Watershed Segmentation')
    plt.axis('off')
    plt.show()
    return color

# ========== COMPARISON ==========
def compare_segmentation_methods(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    results = {}

    _, otsu = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    results['Otsu Thresholding'] = otsu

    edges = cv2.Canny(image, 100, 200)
    results['Canny Edge Detection'] = edges

    color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    ret, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    kernel = np.ones((3,3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
    sure_bg = cv2.dilate(opening, kernel, iterations=3)
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)
    ret, markers = cv2.connectedComponents(sure_fg)
    markers = markers + 1
    markers[unknown == 255] = 0
    markers = cv2.watershed(color, markers)
    color[markers == -1] = [255,0,0]
    results['Watershed'] = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)

    plt.figure(figsize=(15,5))
    for i, (name, result) in enumerate(results.items(), 1):
        plt.subplot(1,3,i)
        plt.imshow(result, cmap='gray')
        plt.title(name)
        plt.axis('off')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    image_path = 'img2.jpg'  # Ganti dengan path gambar kamu
    sobel_edge_detection(image_path)
    canny_edge_detection(image_path)
    watershed_segmentation(image_path)
    compare_segmentation_methods(image_path)
