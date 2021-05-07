from scipy.ndimage import maximum_filter, minimum_filter

def midpoint(img):
    maxf = maximum_filter(img, (3, 3))
    minf = minimum_filter(img, (3, 3))
    midpoint = (maxf + minf) / 2
    cv2_imshow(midpoint)
print("\n\n---Effects on S&P Noise Image with Probability 0.5---\n\n")
midpoint(sp_05)
