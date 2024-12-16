import ezdxf
import sys
import matplotlib.pyplot as plt
from ezdxf import recover
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend


def dxf_to_jpg(dxf_filepath):
    """
    Модуль переводит файл DXF в JPG
    :param dxf_filepath:
    :param jpg_filepath:
    :return:
    """
    try:
        doc, auditor = recover.readfile(dxf_filepath)
    except IOError:
        print(f'Not a DXF file or a generic I/O error.')
        sys.exit(1)
    except ezdxf.DXFStructureError:
        print(f'Invalid or corrupted DXF file.')
        sys.exit(2)

    # The auditor.errors attribute stores severe errors,
    # which may raise exceptions when rendering.
    if not auditor.has_errors:
        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])
        ctx = RenderContext(doc)
        out = MatplotlibBackend(ax)
        Frontend(ctx, out).draw_layout(doc.modelspace(), finalize=True)
        jpg_filepath = dxf_filepath[:-4]+'.png'
        fig.savefig(jpg_filepath, dpi=300)


if __name__ == '__main__':
    dxf_file = "drawing.dxf"  # Replace with your DXF file path
    dxf_to_jpg(dxf_file)
