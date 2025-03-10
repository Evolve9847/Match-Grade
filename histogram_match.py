import numpy as np
import cv2

def match_histograms(source, reference):
    """Match the histogram of the source image to the reference image."""
    source_lab = cv2.cvtColor(source, cv2.COLOR_RGB2LAB)
    reference_lab = cv2.cvtColor(reference, cv2.COLOR_RGB2LAB)

    matched_lab = np.zeros_like(source_lab)

    for i in range(3):  # Apply histogram matching for L, A, and B channels
        src_hist, bins = np.histogram(source_lab[..., i].ravel(), 256, [0, 256])
        ref_hist, _ = np.histogram(reference_lab[..., i].ravel(), 256, [0, 256])

        cdf_src = np.cumsum(src_hist).astype(float)
        cdf_src /= cdf_src[-1]

        cdf_ref = np.cumsum(ref_hist).astype(float)
        cdf_ref /= cdf_ref[-1]

        lookup_table = np.interp(cdf_src, cdf_ref, np.arange(256))
        matched_lab[..., i] = cv2.LUT(source_lab[..., i], lookup_table.astype(np.uint8))

    return cv2.cvtColor(matched_lab, cv2.COLOR_LAB2RGB)
