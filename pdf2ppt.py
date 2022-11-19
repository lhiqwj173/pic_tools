from pdf import pdf_to_ppt
from tool import apply_all
import os

if __name__ == "__main__":
    apply_all(pdf_to_ppt, os.path.split(os.path.realpath(__file__))[0])
