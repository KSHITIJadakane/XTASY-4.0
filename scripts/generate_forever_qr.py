import qrcode
from PIL import Image, ImageDraw, ImageFont
import os
import shutil

url = "https://xtasy-4-0.vercel.app"
logo_path = "assets/xtasy_logo.jpg"
output_dir = "assets"
os.makedirs(output_dir, exist_ok=True)

print(f"Generating permanent (forever) static QR codes for: {url}")

# -------------------------------------------------------------
# 1. Classic High-Res Black & White QR
# -------------------------------------------------------------
qr_classic = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=32,
    border=4,
)
qr_classic.add_data(url)
qr_classic.make(fit=True)
img_classic = qr_classic.make_image(fill_color="black", back_color="white").convert("RGBA")
classic_path = os.path.join(output_dir, "xtasy_qr_classic.png")
img_classic.save(classic_path)
print(f"Saved: {classic_path} ({img_classic.size[0]}x{img_classic.size[1]})")

# -------------------------------------------------------------
# 2. Branded QR with Center XTASY 4.0 Circular Logo Badge
# -------------------------------------------------------------
qr_branded = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=32,
    border=4,
)
qr_branded.add_data(url)
qr_branded.make(fit=True)
img_branded = qr_branded.make_image(fill_color="#0a0a0a", back_color="#ffffff").convert("RGBA")

# Load and prepare the logo
if os.path.exists(logo_path):
    logo = Image.open(logo_path).convert("RGBA")
    
    # Calculate logo size: ~22% of QR width for optimal scannability with Level H (30% tolerance)
    qr_w, qr_h = img_branded.size
    logo_size = int(qr_w * 0.22)
    logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
    
    # Create circular mask for logo
    mask = Image.new("L", (logo_size, logo_size), 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.ellipse((0, 0, logo_size, logo_size), fill=255)
    
    # Create circular white background pad with pink rim
    pad_border = 14
    pad_size = logo_size + pad_border * 2
    pad = Image.new("RGBA", (pad_size, pad_size), (0, 0, 0, 0))
    draw_pad = ImageDraw.Draw(pad)
    draw_pad.ellipse((0, 0, pad_size - 1, pad_size - 1), fill="#ffffff", outline="#BA134D", width=6)
    
    # Paste logo into pad
    pad.paste(logo, (pad_border, pad_border), mask)
    
    # Center position
    pos = ((qr_w - pad_size) // 2, (qr_h - pad_size) // 2)
    img_branded.paste(pad, pos, pad)
    
branded_path = os.path.join(output_dir, "xtasy_qr_branded.png")
img_branded.save(branded_path)
print(f"Saved: {branded_path} ({img_branded.size[0]}x{img_branded.size[1]})")

# -------------------------------------------------------------
# 3. Stylized XTASY 4.0 Poster / Social Card (1200 x 1650)
# -------------------------------------------------------------
card_w, card_h = 1200, 1650
card = Image.new("RGBA", (card_w, card_h), "#050505")
draw_card = ImageDraw.Draw(card)

# Subtle border with Squid Game neon pink glow
draw_card.rectangle([(20, 20), (card_w - 20, card_h - 20)], outline="#BA134D", width=4)
draw_card.rectangle([(28, 28), (card_w - 28, card_h - 28)], outline="#333333", width=1)

# Shapes at top: ○ △ □
symbols = "○   △   □"
try:
    font_symbols = ImageFont.truetype("arial.ttf", 40)
    font_title = ImageFont.truetype("arial.ttf", 68)
    font_sub = ImageFont.truetype("arial.ttf", 26)
    font_url = ImageFont.truetype("arial.ttf", 32)
    font_call = ImageFont.truetype("arial.ttf", 36)
except:
    font_symbols = font_title = font_sub = font_url = font_call = ImageFont.load_default()

# Header text
draw_card.text((card_w // 2, 85), symbols, fill="#BA134D", font=font_symbols, anchor="mm")
draw_card.text((card_w // 2, 165), "XTASY 4.0", fill="#ffffff", font=font_title, anchor="mm")
draw_card.text((card_w // 2, 235), "DEPARTMENT OF INDUSTRIAL IOT", fill="#00F0FF", font=font_sub, anchor="mm")
draw_card.text((card_w // 2, 280), "THE HIGH-STAKES QUEST ROOM ARENA", fill=(255, 255, 255, 180), font=font_sub, anchor="mm")

# Place branded QR in the center of card
qr_display = img_branded.resize((760, 760), Image.Resampling.LANCZOS)
card.paste(qr_display, ((card_w - 760) // 2, 360))

# Bottom CTA & Link
draw_card.text((card_w // 2, 1200), "SCAN TO ENTER THE GAME", fill="#BA134D", font=font_call, anchor="mm")
draw_card.text((card_w // 2, 1275), url, fill="#ffffff", font=font_url, anchor="mm")
draw_card.text((card_w // 2, 1345), "HOLD THE CARD  •  ACCEPT THE CHALLENGE", fill=(255, 255, 255, 140), font=font_sub, anchor="mm")

# Footer brand
draw_card.text((card_w // 2, 1550), "○   △   □", fill="#00F0FF", font=font_symbols, anchor="mm")

poster_path = os.path.join(output_dir, "xtasy_qr_poster.png")
card.save(poster_path)
print(f"Saved: {poster_path} ({card_w}x{card_h})")

# -------------------------------------------------------------
# 4. SVG Vector QR Code (Infinite resolution for printing)
# -------------------------------------------------------------
try:
    import qrcode.image.svg
    factory = qrcode.image.svg.SvgPathImage
    qr_svg = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
        image_factory=factory
    )
    qr_svg.add_data(url)
    qr_svg.make(fit=True)
    svg_img = qr_svg.make_image()
    svg_path = os.path.join(output_dir, "xtasy_qr_code.svg")
    svg_img.save(svg_path)
    print(f"Saved: {svg_path} (Vector format)")
except Exception as e:
    print("SVG Generation skipped:", e)

# -------------------------------------------------------------
# 5. Copy all files to artifacts directory for direct user preview
# -------------------------------------------------------------
artifacts_dir = r"C:\Users\rajur\.gemini\antigravity-ide\brain\ea9f7c0a-b2b2-4497-ae56-78ee48235d1b"
for f in ["xtasy_qr_branded.png", "xtasy_qr_classic.png", "xtasy_qr_poster.png", "xtasy_qr_code.svg"]:
    sp = os.path.join(output_dir, f)
    if os.path.exists(sp):
        dp = os.path.join(artifacts_dir, f)
        shutil.copy2(sp, dp)
        print(f"Copied to artifact: {dp}")

print("\nAll permanent QR codes generated successfully!")
