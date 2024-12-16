import ezdxf
from pathlib import Path


def insert_dxf_entities(target_dxf_path, source_dxf_path, offset=(0, 0, 0)):
    """
    Inserts all entities from a source DXF file into a target DXF file with an offset.

    Args:
        target_dxf_path (str or Path): Path to the target DXF file.
        source_dxf_path (str or Path): Path to the source DXF file.
        offset (tuple): A 3D offset (dx, dy, dz) to apply to all entities.

    Returns:
        bool: True if successful, False otherwise. Prints informative messages.
    """
    target_dxf_path = Path(target_dxf_path)
    source_dxf_path = Path(source_dxf_path)

    if not target_dxf_path.exists():
        print(f"Error: Target DXF file '{target_dxf_path}' not found.")
        return False
    if not source_dxf_path.exists():
        print(f"Error: Source DXF file '{source_dxf_path}' not found.")
        return False

    try:
        target_doc = ezdxf.readfile(target_dxf_path)
        source_doc = ezdxf.readfile(source_dxf_path)
        target_msp = target_doc.modelspace()

        dx, dy, dz = offset  # Unpack the offset tuple

        for entity in source_doc.modelspace():
            try:
                new_entity = entity.copy()
                new_entity.translate(dx, dy, dz)  # Correctly apply the offset
                target_msp.add_entity(new_entity)
            except Exception as e:
                print(f"Error inserting entity {entity.dxftype()}: {e}")
                # You might choose to continue even if some entities fail to insert
                # return False  #Uncomment to stop on first error

        target_doc.saveas(target_dxf_path)
        print(f"Entities from '{source_dxf_path}' successfully inserted into '{target_dxf_path}'.")
        return True

    except ezdxf.errors.DXFStructureError:
        print(f"Error: Invalid or corrupted DXF file.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False


# Example usage:
target_dxf = "20241210_140951.dxf"
source_dxf = "latch.dxf"
offset = (183, 800, 0)  # Example offset
success = insert_dxf_entities(target_dxf, source_dxf, offset)

if success:
    print("Insertion successful!")
    #         _, _, text_width, text_height_actual = draw.textbbox((0, 0), text=text_to_add, font=font)
