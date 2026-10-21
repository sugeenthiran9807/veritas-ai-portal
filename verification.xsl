<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
<html>
<head>
    <title>AI Content Verification Portal</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #eef5ff; padding: 20px; }
        table { width: 90%; margin: auto; border-collapse: collapse; background: white; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-radius: 8px; overflow: hidden; }
        th { background-color: #2c3e50; color: white; padding: 14px; text-align: left; }
        td { padding: 12px 14px; border: 1px solid #ddd; }
        tr:nth-child(even) { background-color: #f9fbff; }
        h2 { color: #2c3e50; text-align: center; margin-bottom: 25px; }
    </style>
</head>
<body>
    <h2>AI CONTENT AUTHENTICITY &amp; VERIFICATION PORTAL</h2>
    <table>
        <tr>
            <th>Report No</th>
            <th>Title</th>
            <th>Category</th>
            <th>Verification Score</th>
            <th>Time</th>
            <th>Auditor</th>
        </tr>
        <xsl:for-each select="verification/report">
        <tr>
            <td><xsl:value-of select="reportno"/></td>
            <td><b><xsl:value-of select="title"/></b></td>
            <td><xsl:value-of select="category"/></td>
            <td><xsl:value-of select="score"/></td>
            <td><xsl:value-of select="time"/></td>
            <td><xsl:value-of select="author/authorname"/> (<xsl:value-of select="author/designation"/>)</td>
        </tr>
        </xsl:for-each>
    </table>
</body>
</html>
</xsl:template>
</xsl:stylesheet>
