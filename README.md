# VERITAS — AI Content Verification & Authenticity Platform
**Web Technologies Laboratory (Course Code: CCS375 / Registration Code: 9807)**

---

## 🌟 Executive Summary

**VERITAS** is a multi-tier, multimodal forensic platform engineered to detect, audit, and verify synthetic, AI-manipulated, and human-authored digital assets across images, video, audio, text, and structured data feeds.

Based on the lab manual and project record, this application integrates seven key laboratory exercises into a unified, high-performance web suite with an enterprise cyber-forensic interface.

---

## 📁 Repository Structure

```
veritas_ai_portal/
├── index.html          # 🌟 Flagship Unified Veritas AI Portal (Ex 1 to Ex 7 all-in-one)
├── scan.html           # ▣ Multimodal Media Signal Scanner (Ex 1)
├── detector.html       # 📝 DHTML Client-Side AI Text Detector (Ex 3)
├── session.html        # ⏱️ HttpSession Investigator Tracking Portal (Ex 5B)
├── marklist.html       # 📊 Three-Tier Student Examination Mark Query (Ex 6B)
├── reports.html        # 📑 XML / XSLT / CSS Authenticated Report Feeds (Ex 7)
├── photo.html          # ◇ Photo Signal Profile (Pixel & Noise Analysis) (Ex 2)
├── video.html          # ▶ Video Signal Profile (Frame & Cadence Analysis) (Ex 2)
├── audio.html          # ◐ Audio Signal Profile (Spectral & Pitch Analysis) (Ex 2)
├── archive.html        # ☰ Signal Trail & Audit History (Ex 2)
├── index.jsp           # Candidate Examination Portal Entrypoint (Ex 6A)
├── web.xml             # Jakarta EE 6.0 Servlet Deployment Descriptor
├── database.sql        # SQL Server / MySQL Database Schema & Seed Data (Ex 6B)
├── verification.xml    # Official XML Report Catalog (Ex 7)
├── verification.dtd    # Document Type Definition Schema Validator (Ex 7)
├── verification.xsd    # W3C XML Schema Definition (Ex 7)
├── verification.css    # XML CSS Presentation Stylesheet (Ex 7)
├── verification.xsl    # XSL Transformation Stylesheet (Ex 7)
├── server.py           # Python 3.13 Local Web Server & Servlet Emulator (Port 8080)
└── README.md           # Complete Documentation & Lab Reference
```

---

## 🔬 Mapping of Laboratory Exercises

| Ex No. | Title & Objective | Technologies Used | Corresponding File(s) |
| :--- | :--- | :--- | :--- |
| **Ex 1** | Image Maps & Multimodal Signal Detection | HTML5, DHTML, File API, Canvas | `scan.html`, `index.html` (Scanner Tab) |
| **Ex 2** | CSS Layout, Nav Rail, & Signal Maps | CSS3 Flexbox/Grid, SVG, Gradients | `index.html`, `photo.html`, `video.html`, `audio.html`, `archive.html` |
| **Ex 3** | Client-Side Form Validation & Heuristic AI Detector | DHTML, RegEx, Conic Gradients | `detector.html`, `index.html` (Detector Tab) |
| **Ex 5A** | Invoking Jakarta Servlets from HTML Forms | HttpServlet, doPost, Form Controls | `audit.html`, `index.html` (Audit Tab) |
| **Ex 5B** | Session Tracking using HttpSession | HttpSession, Cookies, Visit Counters | `session.html`, `index.html` (Session Tab) |
| **Ex 6A** | Three-Tier Examination Web Application | Jakarta Servlets, Multipage Assessment | `index.jsp`, `index.html` (Exam Tab) |
| **Ex 6B** | Three-Tier Student Marks via JSP & Database | JSP, JDBC PreparedStatement, SQL | `marklist.html`, `database.sql`, `index.html` (Marklist Tab) |
| **Ex 7** | XML, DTD, XML Schema, XSLT, & CSS Reports | XML, DTD, XSD, XSLT, CSS3 | `verification.xml`, `verification.xsd`, `verification.xsl`, `reports.html` |
| **Server** | Apache Tomcat 10 Setup & Deployment | Tomcat 10, Port 8080, JDK 17 | `server.py`, `web.xml` |

---

## 🚀 How to Run the Website

### Option 1: Instant Client-Side Launch (Zero Dependencies)
Double-click `index.html` in Windows Explorer or open it in any modern browser (Chrome, Edge, Firefox, Opera, Brave). All modules, local databases, forensic scanners, and interactive features run 100% offline via modern Web APIs!

### Option 2: Run with Python Server (Port 8080)
To run on the standard Apache Tomcat port (`8080`):
```powershell
python server.py
```
Then navigate to:
```
http://localhost:8080
```
This emulates Jakarta Servlets (`/AIContentVerifyServlet`, `/SessionTracking`, `/marklist.jsp`) and serves all static assets.

### Option 3: Deploy to Apache Tomcat 10
1. Copy the `veritas_ai_portal` directory into your Tomcat installation directory:
   ```
   C:\Program Files\Apache Software Foundation\Tomcat 10.1\webapps\AIContentVerification\
   ```
2. Start the Tomcat service or launch `bin\startup.bat`.
3. Open `http://localhost:8080/AIContentVerification/`.

---

## 📊 Database Configuration (Ex 6B)

The database table `student_exam` is pre-seeded with the exact lab manual records:

| Register No | Candidate Name | Exam Title | Score | Result |
| :--- | :--- | :--- | :--- | :--- |
| **9807** | SUGEENTHIRAN | AI Content Verification Examination | 5 / 5 | **PASS** |
| **9947** | M. MOHAMED ZAID | AI Content Verification Examination | 5 / 5 | **PASS** |
| **9948** | ROOH | AI Content Verification Examination | 5 / 5 | **PASS** |
| **9949** | NOOR | AI Content Verification Examination | 4 / 5 | **PASS** |
| **9950** | AIRA | AI Content Verification Examination | 3 / 5 | **PASS** |
| **9951** | MEER | AI Content Verification Examination | 5 / 5 | **PASS** |
| **9952** | AYAN | AI Content Verification Examination | 2 / 5 | **FAIL** |
| **9087654321** | Riya Sharma | AI Content Verification Examination | 5 / 5 | **PASS** |

To populate in SQL Server or MySQL, execute `database.sql`.

---

## 🏆 Key Features Implemented

1. **Interactive Signal Map (Ex 2)**: Dynamic SVG nodes connecting Veritas AI Core to Photo (Pixel Signal), Video (Frame Signal), and Audio (Voice Signal) with interactive forensic modal profiles.
2. **Multimodal Media Scanner (Ex 1)**: Supports drag-and-drop of photos, videos, and audio. Features live Fourier noise overlay filters, animated equalizer visualizer, and confidence calculation.
3. **DHTML Real-time AI Text Detector (Ex 3)**: Features live character and word counters, formulaic AI transition word detection, and dynamic 360-degree conic gradient gauge.
4. **Certified Forensic Audit Reports (Ex 5A)**: Generates verified digital audit cards with Perplexity Index, Burstiness Variance, and RSA authentication hashes.
5. **Session Tracking (Ex 5B)**: Persistent session tracking maintaining visitor counts and access timestamps across page reloads.
6. **Online Examination & Certification (Ex 6A)**: 5-question AI Content Verification exam with instant grading, pass/fail evaluation, and automatic database score sync.
7. **XML & XSLT Intelligence Feeds (Ex 7)**: Dual-view reporting supporting XSLT tabular format, CSS card layout, and live schema validation.
