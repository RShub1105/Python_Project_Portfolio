from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
def create_resume(name,contact,summary,skills,experience,education):
    c = canvas.Canvas("resume.pdf",pagesize=LETTER)
    width,height = LETTER
    
    y = height-50
    
    def draw_line(text,size=12,bold=False):
        nonlocal y
        if bold:
            c.setFont("Helvetica-Bold",size)
        else:
            c.setFont("Helvetica",size)
        c.drawString(50,y,text)
        y-=20
    
    draw_line(name,18,bold=True)
    draw_line(contact,12)
    
    y-=10
    draw_line("SUMMARY",14,bold=True)
    draw_line(summary)

    y-=10
    draw_line("SKILLS",14,bold=True)
    for skill in skills:
        draw_line(f"-{skill}")

    y-=10
    draw_line("EXPERIENCE",14,bold=True)
    for exp in experience:
        draw_line(f"-{exp}")

    y-=10
    draw_line("EDUCATION",14,bold=True)
    for edu in education:
        draw_line(f"-{edu}")
    c.save()
    print("Resume generated as 'resume.pdf'")

create_resume( 
    name="Your Name", 
    contact="Email | Phone",
    summary="A passionate Python developer with interest in automation and backend development.",
    skills=["intern in amazon - Python script for logs","build cli tools and api"],
    experience=["Worked on automating daily reports", "Developed backend APIs using Flask"],
    education=["BCA in computer application - kolhan university","completed 17 day python challenge"]
)