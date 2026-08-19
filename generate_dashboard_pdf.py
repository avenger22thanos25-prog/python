import os
import platform
import subprocess
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak

def build_presentation_pdf(filename="MarketMind_AI_Dashboard_Presentation.pdf"):
    # Setup Document in Landscape Orientation (11 x 8.5 inches)
    doc = SimpleDocTemplate(
        filename,
        pagesize=landscape(letter),
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Palette
    NAVY = colors.HexColor("#1A237E")
    DARK_BLUE = colors.HexColor("#0D47A1")
    LIGHT_BG = colors.HexColor("#F5F7FA")
    ACCENT_BLUE = colors.HexColor("#0288D1")
    WHITE = colors.HexColor("#FFFFFF")
    TEXT_DARK = colors.HexColor("#212121")
    
    # Custom Typography Styles
    title_style = ParagraphStyle('DocTitle', parent=styles['Title'], fontSize=28, leading=34, textColor=NAVY, alignment=0)
    subtitle_style = ParagraphStyle('DocSubtitle', parent=styles['Normal'], fontSize=14, leading=18, textColor=ACCENT_BLUE)
    slide_header = ParagraphStyle('SlideHeader', parent=styles['Heading1'], fontSize=20, leading=24, textColor=NAVY, spaceAfter=10)
    body_bold = ParagraphStyle('BodyBold', parent=styles['Normal'], fontSize=10, leading=13, fontName="Helvetica-Bold", textColor=TEXT_DARK)
    body_style = ParagraphStyle('BodyTextCustom', parent=styles['Normal'], fontSize=9, leading=12, textColor=TEXT_DARK)
    card_title = ParagraphStyle('CardTitle', parent=styles['Normal'], fontSize=11, leading=14, fontName="Helvetica-Bold", textColor=WHITE)

    story = []

    # SLIDE 1: TITLE SLIDE
    story.append(Paragraph("MarketMind AI", title_style))
    story.append(Paragraph("Small Business Sales Intelligence Platform — Research Dashboard Layouts", subtitle_style))
    story.append(Spacer(1, 20))
    
    intro_p = Paragraph(
        "<b>Project Objective:</b> Build a full-stack AI-powered sales intelligence platform to help businesses "
        "monitor performance, track inventory, manage invoices, and generate predictive insights using machine learning.<br/><br/>"
        "<b>Dashboard Concept:</b> Role-Based UI layout tailored for Business Owners, Store Managers, Sales Executives, and System Administrators.",
        body_style
    )
    
    intro_table = Table([[intro_p]], colWidths=[720])
    intro_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('PADDING', (0,0), (-1,-1), 16),
        ('BOX', (0,0), (-1,-1), 1, ACCENT_BLUE),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(intro_table)
    story.append(Spacer(1, 30))

    tech_text = Paragraph("<b>Core Tech Stack:</b> FastAPI (Backend) | ReactJS / Streamlit (Frontend) | PostgreSQL / SQLite | Scikit-Learn & Prophet (AI Engine)", body_style)
    tech_table = Table([[tech_text]], colWidths=[720])
    tech_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), NAVY),
        ('TEXTCOLOR', (0,0), (-1,-1), WHITE),
        ('PADDING', (0,0), (-1,-1), 10),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(tech_table)
    story.append(PageBreak())

    # SLIDE 2: BUSINESS OWNER DASHBOARD VIEW
    story.append(Paragraph("1. Business Owner Dashboard View (Executive Strategy)", slide_header))
    story.append(Paragraph("Primary Focus: High-level strategic decisions, sales forecasting, and churn analysis.", body_style))
    story.append(Spacer(1, 10))

    kpi1 = Paragraph("<b>Total Revenue Today</b><br/><font size=14 color='#1A237E'><b>$12,450</b></font>", body_bold)
    kpi2 = Paragraph("<b>Predicted Growth (Q3)</b><br/><font size=14 color='#2E7D32'><b>+18.4%</b></font>", body_bold)
    kpi3 = Paragraph("<b>At-Risk Customers</b><br/><font size=14 color='#C62828'><b>14 Users</b></font>", body_bold)
    
    kpi_table = Table([[kpi1, kpi2, kpi3]], colWidths=[230, 230, 230])
    kpi_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('BOX', (0,0), (-1,-1), 1, colors.lightgrey),
        ('PADDING', (0,0), (-1,-1), 10),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(kpi_table)
    story.append(Spacer(1, 15))

    panel1_title = Paragraph("<b>MAIN PANEL: Sales Forecasting Engine</b>", card_title)
    panel1_desc = Paragraph(
        "• <b>Algorithm:</b> Prophet / XGBoost Regressor<br/>"
        "• <b>Visual:</b> Time-series line chart with solid historical data vs shaded prediction band.<br/>"
        "• <b>Controls:</b> Date range selector, category filter, seasonal trend toggles.",
        body_style
    )
    
    panel2_title = Paragraph("<b>SECONDARY PANEL: Churn Prediction</b>", card_title)
    panel2_desc = Paragraph(
        "• <b>Algorithm:</b> Random Forest / XGBoost<br/>"
        "• <b>Visual:</b> List of high-value customers at risk of inactivity.<br/>"
        "• <b>Output:</b> Risk probability score + retention recommendations.",
        body_style
    )

    t_p1 = Table([[panel1_title], [panel1_desc]], colWidths=[350])
    t_p1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY),
        ('BACKGROUND', (0,1), (-1,1), LIGHT_BG),
        ('PADDING', (0,0), (-1,-1), 10),
        ('BOX', (0,0), (-1,-1), 1, NAVY),
    ]))

    t_p2 = Table([[panel2_title], [panel2_desc]], colWidths=[350])
    t_p2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BLUE),
        ('BACKGROUND', (0,1), (-1,1), LIGHT_BG),
        ('PADDING', (0,0), (-1,-1), 10),
        ('BOX', (0,0), (-1,-1), 1, DARK_BLUE),
    ]))

    body_layout = Table([[t_p1, t_p2]], colWidths=[360, 360])
    body_layout.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP')]))
    story.append(body_layout)
    story.append(PageBreak())

    # SLIDE 3: STORE MANAGER DASHBOARD VIEW
    story.append(Paragraph("2. Store Manager Dashboard View (Operations & Inventory)", slide_header))
    story.append(Paragraph("Primary Focus: Daily inventory management, stock alerts, and anomaly detection.", body_style))
    story.append(Spacer(1, 10))

    kpi_m1 = Paragraph("<b>Total Inventory Value</b><br/><font size=14 color='#1A237E'><b>$84,200</b></font>", body_bold)
    kpi_m2 = Paragraph("<b>Reorder Alerts</b><br/><font size=14 color='#EF6C00'><b>5 Items</b></font>", body_bold)
    kpi_m3 = Paragraph("<b>Inventory Anomalies</b><br/><font size=14 color='#C62828'><b>2 Flagged</b></font>", body_bold)
    
    kpi_table_m = Table([[kpi_m1, kpi_m2, kpi_m3]], colWidths=[230, 230, 230])
    kpi_table_m.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('BOX', (0,0), (-1,-1), 1, colors.lightgrey),
        ('PADDING', (0,0), (-1,-1), 10),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(kpi_table_m)
    story.append(Spacer(1, 15))

    op1_title = Paragraph("<b>MAIN PANEL: Stock Tracking & Warehouse Matrix</b>", card_title)
    op1_desc = Paragraph(
        "• Progress bar indicators for stock levels (Green: OK, Orange: Low, Red: Critical).<br/>"
        "• Instant action button for threshold-based reordering alerts.<br/>"
        "• Multi-warehouse inventory logs.",
        body_style
    )
    
    op2_title = Paragraph("<b>SECONDARY PANEL: Anomaly Detection System</b>", card_title)
    op2_desc = Paragraph(
        "• <b>Algorithm:</b> Isolation Forest / Statistical Outlier Detection<br/>"
        "• Highlights unusual sales transactions and inventory loss.<br/>"
        "• Real-time alert generation for suspicious activities.",
        body_style
    )

    t_op1 = Table([[op1_title], [op1_desc]], colWidths=[350])
    t_op1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY),
        ('BACKGROUND', (0,1), (-1,1), LIGHT_BG),
        ('PADDING', (0,0), (-1,-1), 10),
        ('BOX', (0,0), (-1,-1), 1, NAVY),
    ]))

    t_op2 = Table([[op2_title], [op2_desc]], colWidths=[350])
    t_op2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BLUE),
        ('BACKGROUND', (0,1), (-1,1), LIGHT_BG),
        ('PADDING', (0,0), (-1,-1), 10),
        ('BOX', (0,0), (-1,-1), 1, DARK_BLUE),
    ]))

    op_layout = Table([[t_op1, t_op2]], colWidths=[360, 360])
    op_layout.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP')]))
    story.append(op_layout)
    story.append(PageBreak())

    # SLIDE 4: SALES EXECUTIVE & SYSTEM ADMIN DASHBOARDS
    story.append(Paragraph("3. Sales Executive & Admin Dashboard Views", slide_header))
    story.append(Spacer(1, 10))

    se_title = Paragraph("<b>Sales Executive View (Transactions & POS)</b>", card_title)
    se_desc = Paragraph(
        "• <b>Sales Data Upload:</b> Fast CSV import and transaction storage.<br/>"
        "• <b>Invoice Management:</b> Create, track, and monitor payment statuses.<br/>"
        "• <b>Product Recommendation Engine:</b> Collaborative Filtering & Association Rules for real-time cross-sell/upsell suggestions.",
        body_style
    )

    admin_title = Paragraph("<b>System Administrator View (Platform Management)</b>", card_title)
    admin_desc = Paragraph(
        "• <b>User & Role Management:</b> Enforce Role-Based Access Control (RBAC).<br/>"
        "• <b>AI Module Configuration:</b> Monitor ML models, view evaluation metrics (MAE, RMSE, Precision, F1-Score).<br/>"
        "• <b>System Security:</b> Audit logging, API rate limiting, database status.",
        body_style
    )

    t_se = Table([[se_title], [se_desc]], colWidths=[350])
    t_se.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY),
        ('BACKGROUND', (0,1), (-1,1), LIGHT_BG),
        ('PADDING', (0,0), (-1,-1), 10),
        ('BOX', (0,0), (-1,-1), 1, NAVY),
    ]))

    t_admin = Table([[admin_title], [admin_desc]], colWidths=[350])
    t_admin.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BLUE),
        ('BACKGROUND', (0,1), (-1,1), LIGHT_BG),
        ('PADDING', (0,0), (-1,-1), 10),
        ('BOX', (0,0), (-1,-1), 1, DARK_BLUE),
    ]))

    final_layout = Table([[t_se, t_admin]], colWidths=[360, 360])
    final_layout.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP')]))
    story.append(final_layout)

    # Build Document
    doc.build(story)
    print(f"✅ Success! PDF created at: {filename}")

if __name__ == "__main__":
    filename = "MarketMind_AI_Dashboard_Presentation.pdf"
    build_presentation_pdf(filename)
    
    # Auto-open PDF on execution
    try:
        if platform.system() == 'Windows':
            os.startfile(filename)
        elif platform.system() == 'Darwin':  # macOS
            subprocess.call(('open', filename))
        else:  # Linux
            subprocess.call(('xdg-open', filename))
    except Exception as e:
        print(f"File created, but could not auto-open: {e}")