import pydicom
import numpy as np
import io
import os
from pydantic import validate_call

threshold_value = float(os.environ.get('THRESHOLD_VALUE', '0.5'))

@validate_call
def calculate_volume_from_dicom(image_data: bytes) -> float:
    # Load the DICOM file
    dicom_data = pydicom.dcmread(io.BytesIO(image_data))

    # Extract pixel data
    pixel_data = dicom_data.pixel_array

    # Normalize pixel data to [0, 1]
    max_pixel_value = np.max(pixel_data)
    min_pixel_value = np.min(pixel_data)
    normalized_pixel_data = (pixel_data - min_pixel_value) / (max_pixel_value - min_pixel_value)

    # Threshold the normalized pixel data
    thresholded_data = normalized_pixel_data > threshold_value

    # Calculate pixel volume in cubic millimeters
    pixel_spacing = dicom_data.PixelSpacing  # [row spacing, column spacing] in mm/pixel
    slice_thickness = dicom_data.SliceThickness  # slice thickness in mm
    voxel_volume = pixel_spacing[0] * pixel_spacing[1] * slice_thickness
    volume_mm3 = np.sum(thresholded_data) * voxel_volume

    return volume_mm3
