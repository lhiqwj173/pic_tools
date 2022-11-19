import aspose.slides as slides
import fitz
import os


def pdf_to_png(pdfPath):
    # 文件格式检查
    if os.path.splitext(pdfPath)[-1] != '.pdf':
        return

    # 打开PDF文件
    pdf = fitz.open(pdfPath)

    # 逐页读取PDF
    for pg in range(0, pdf.page_count):
        page = pdf[pg]
        # 设置缩放和旋转系数
        # trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotation_angle)
        pm = page.get_pixmap(dpi=600, alpha=True)
        # 开始写图像
        pm.save(pdfPath.replace('.pdf', f'_{pg}.png'))

    if pdf.page_count == 1:
        os.rename(pdfPath.replace(
            '.pdf', f'_{0}.png'), pdfPath.replace('.pdf', f'.png'))

    pdf.close()


def pdf_to_ppt(pdfPath):
    # 文件格式检查
    if os.path.splitext(pdfPath)[-1] != '.pdf':
        return

    # Create presentation
    with slides.Presentation() as pres:

        # Remove default slide from presentation
        pres.slides.remove_at(0)

        # Import PDF to presentation
        pres.slides.add_from_pdf(pdfPath)

        # Save presentation
        pres.save(pdfPath.replace('.pdf', '.pptx'),
                  slides.export.SaveFormat.PPTX)
