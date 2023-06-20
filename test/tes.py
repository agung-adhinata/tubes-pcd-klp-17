import numpy as np
from matplotlib import pyplot as plt
from skimage.feature import graycomatrix, graycoprops
image = np.array([[0, 0, 1, 1],
                  [0, 0, 1, 1],
                  [0, 2, 2, 2],
                  [2, 2, 3, 3]], dtype=np.uint8)

d45 = np.pi / 8
d90 = np.pi / 4
d135 = d90 + d45

result = graycomatrix(
    image, [1], [0, d45, d90, d135], symmetric=True, levels=8, normed=True)
# plt.figure(figsize=(10, 10))
# plt.subplot(2, 2, 1)
# plt.title("0 deg")
# plt.imshow(result[:, :, 0, 0], 'gray')
# plt.subplot(2, 2, 2)
# plt.title("45 deg")
# plt.imshow(result[:, :, 0, 1], 'gray')
# plt.subplot(2, 2, 3)
# plt.title("90 deg")
# plt.imshow(result[:, :, 0, 2], 'gray')
# plt.subplot(2, 2, 4)
# plt.title("135 deg")
# plt.imshow(result[:, :, 0, 3], 'gray')
# plt.show()

res = []
end = []
properties = ['dissimilarity', 'correlation',
              'homogeneity', 'contrast', 'ASM', 'energy']
out = [props for item in properties for props in graycoprops(result, item)[0]]
res.append(out)
for item in res:
    end.append(item)
print(item)
print(type(item))
