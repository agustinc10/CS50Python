from fpdf import FPDF, Align


class PDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 30)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        # self.text(30, 20,text="CS50 Shirtificate")
        self.cell(30, 10, "CS50 Shirtificate", align="C")
        # Performing a line break:
        self.ln(20)


def main():
    name = input("Name: ")

    pdf = PDF()
    pdf.add_page()
    pdf.image("shirtificate.png", x=Align.C, w=pdf.epw)
    pdf.set_font("helvetica", "B", 30)
    pdf.set_text_color(r=255, g=255, b=255)
    pdf.set_auto_page_break(False)
    pdf.cell(0, -250, f"{name} took CS50!", align=Align.C, center=True)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
