#scatter plot
plt.style.use('dark_background')
plt.scatter(x,x**2,label="scatter graph")
plt.legend()

img=cv2.imread('C:/Users/Spardha/Desktop/pyro/back.jpg',0)

print(img)
img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

print(img.shape)

plt.imshow(img

plt.imshow(img1)
plt.axis("off")
plt.show()
crop_img=img1[200:500,200:400]
plt.imshow(crop_img)
plt.axis("off")

crop_img.shape
total_pixels=crop_img.shape[0]*crop_img.shape[1]
print(total_pixels)

cv2.resize(crop_img,(100,100))
plt.title("Beach"+str(crop_img.shape))
plt.imshow(crop_img)
plt.axis("off")
