from PIL import Image, ImageTk
from numpy import average, dot, linalg
List = []
for i in range(9):
    for j in range(9):
        image1 = Image.open('D:\software_practice\get\question(2)' + str(i) + '.jpg')
        image2 = Image.open('D:\software_practice\无框字符\\test(' + str(25) + ')' + str(j) + '.jpg')


        def get_thum(image, size=(64, 64), greyscale=False):
            # 利用image对图像大小重新设置, Image.ANTIALIAS为高质量的
            image = image.resize(size, Image.ANTIALIAS)
            if greyscale:
                # 将图片转换为L模式，其为灰度图，其每个像素用8个bit表示
                image = image.convert('L')
            return image

            # 计算图片的余弦距离


        def image_similarity_vectors_via_numpy(image1, image2):
            image1 = get_thum(image1)
            image2 = get_thum(image2)
            images = [image1, image2]
            vectors = []
            norms = []
            for image in images:
                vector = []
                for pixel_tuple in image.getdata():
                    vector.append(average(pixel_tuple))
                vectors.append(vector)
                # linalg=linear（线性）+algebra（代数），norm则表示范数
                # 求图片的范数
                norms.append(linalg.norm(vector, 2))
            a, b = vectors
            a_norm, b_norm = norms
            # dot返回的是点积，对二维数组（矩阵）进行计算
            res = dot(a / a_norm, b / b_norm)
            return res


        cosin = image_similarity_vectors_via_numpy(image1, image2)
        if cosin > 0.9:
            print(i, j, cosin)
            List.append(j)
print(List)
