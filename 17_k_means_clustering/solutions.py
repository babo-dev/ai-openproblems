import math
import numpy as np


def k_means_numpy(points, k, initial_centroids, max_iterations):
    points = np.array(points)
    centroids = np.array(initial_centroids)

    for _ in range(max_iterations):
        distances = np.linalg.norm(points[:, np.newaxis] - centroids, axis=2)
        labels = np.argmin(distances, axis=1)

        new_centroids = np.array([points[labels == i].mean(axis=0) if np.any(labels == i) else centroids[i]
                                  for i in range(k)])

        if np.allclose(centroids, new_centroids, atol=1e-4):
            break

        centroids = new_centroids

    return [tuple(np.round(centroid, 4)) for centroid in centroids]


def k_means_pure_python(points, k, initial_centroids, max_iterations):
    centroids = initial_centroids.copy()

    for _ in range(max_iterations):
        labels = []
        for point in points:
            distances = [math.sqrt(sum((p - c) ** 2 for p, c in zip(point, centroid))) for centroid in centroids]
            labels.append(distances.index(min(distances)))

        new_centroids = []
        for i in range(k):
            cluster_points = [points[j] for j in range(len(points)) if labels[j] == i]
            if cluster_points:
                centroid = tuple(sum(dim) / len(cluster_points) for dim in zip(*cluster_points))
            else:
                centroid = centroids[i]  # Keep the old centroid if no points are assigned
            new_centroids.append(centroid)

        if all(all(abs(c1 - c2) < 1e-4 for c1, c2 in zip(old, new)) for old, new in zip(centroids, new_centroids)):
            break

        centroids = new_centroids

    return [tuple(round(coord, 4) for coord in centroid) for centroid in centroids]


if __name__ == "__main__":
    points = [(1.0, 2.0), (1.5, 1.8), (5.0, 8.0), (8.0, 8.0), (1.0, 0.6), (9.0, 11.0)]
    initial_centroids = [(1.0, 1.0), (5.0, 5.0)]
    k = 2
    max_iterations = 100

    final_centroids_numpy = k_means_numpy(points, k, initial_centroids, max_iterations)
    print(final_centroids_numpy)

    final_centroids_pure_python = k_means_pure_python(points, k, initial_centroids, max_iterations)
    print(final_centroids_pure_python)
