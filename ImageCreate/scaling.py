import ezdxf
import math


def scale_dxf(dxf_filepath, x_scale, y_scale):
    """Scales a DXF file differentially along the x and y axes.

    Args:
        dxf_filepath: Path to the input DXF file.
        x_scale: Scaling factor for the x-axis.
        y_scale: Scaling factor for the y-axis.
        output_filepath: Path to save the scaled DXF file.
    """
    print(x_scale, y_scale)
    output_filepath = dxf_filepath[:-4]+'_scaled.dxf'
    try:
        doc = ezdxf.readfile(dxf_filepath)
        msp = doc.modelspace()

        for entity in msp:
            if entity.dxftype() == "LINE":
                start_x, start_y, _ = entity.dxf.start
                end_x, end_y, _ = entity.dxf.end
                entity.dxf.start = (start_x * x_scale, start_y * y_scale, 0)
                entity.dxf.end = (end_x * x_scale, end_y * y_scale, 0)
            elif entity.dxftype() == "ARC":
                center_x, center_y, _ = entity.dxf.center
                radius = entity.dxf.radius
                start_angle = entity.dxf.start_angle
                end_angle = entity.dxf.end_angle
                entity.dxf.center = (center_x * x_scale, center_y * y_scale, _)
                entity.dxf.radius = radius * max(x_scale,
                                                 y_scale)  # Maintain aspect ratio for radius.  Alternative scaling methods possible.
            elif entity.dxftype() == "CIRCLE":
                center_x, center_y, _ = entity.dxf.center
                radius = entity.dxf.radius
                entity.dxf.center = (center_x * x_scale, center_y * y_scale)
                entity.dxf.radius = radius * max(x_scale,
                                                 y_scale)  # Maintain aspect ratio for radius.  Alternative scaling methods possible.
            elif entity.dxftype() == "POLYLINE" or entity.dxftype() == "LWPOLYLINE":
                points = entity.get_points()
                scaled_points = [(x * x_scale, y * y_scale, z, a, b) for x, y, z, a, b in points]
                entity.set_points(scaled_points)

        doc.saveas(output_filepath)
        print(f"DXF file '{dxf_filepath}' scaled and saved as '{output_filepath}'")
        return output_filepath

    except FileNotFoundError:
        print(f"Error: DXF file '{dxf_filepath}' not found.")
    except ezdxf.DXFError as e:
        print(f"Error processing DXF file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example Usage
if __name__ == "__main__":
    dxf_file = "20241212_091225.dxf"  # Replace with your DXF file path
    width = 1100
    height = 2200

    x_scale = 1083 / 950
    y_scale = 2118 / 2050

    print(x_scale, y_scale)
    scale_dxf(dxf_file, x_scale, y_scale)
