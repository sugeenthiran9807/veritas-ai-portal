<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html>
<head>
    <title>MZ News and Article - AI Content Verification</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #eef5ff;
            text-align: center;
            padding-top: 80px;
        }
        .container {
            width: 500px;
            margin: auto;
            background-color: white;
            padding: 35px;
            border-radius: 15px;
            box-shadow: 0px 5px 15px #999999;
        }
        h1 {
            color: #2c3e50;
            font-size: 24px;
        }
        h2 {
            color: #1565c0;
            font-size: 18px;
        }
        input[type=text] {
            width: 80%;
            padding: 12px;
            margin: 10px;
            border: 1px solid #999999;
            border-radius: 6px;
            font-size: 14px;
            box-sizing: border-box;
        }
        input[type=submit] {
            background-color: #2c3e50;
            color: white;
            padding: 12px 30px;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            cursor: pointer;
            font-weight: bold;
            transition: 0.2s;
        }
        input[type=submit]:hover {
            background-color: #1a252f;
        }
        p {
            color: #555555;
            font-size: 14px;
        }
        .nav-link {
            display: inline-block;
            margin-top: 20px;
            color: #1565c0;
            text-decoration: none;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>AI Content Verification</h1>
        <h2>Authenticity &amp; Synthetic Text Detection</h2>
        <p>Welcome to the AI Content Verification &amp; Authenticity Portal</p>
        <p>Please enter your details to start the test.</p>
        <form action="exam.html" method="get">
            <input type="text" name="name" placeholder="Enter Your Name" required>
            <br>
            <input type="text" name="regno" placeholder="Enter Register Number" required>
            <br>
            <input type="submit" value="Start Examination">
        </form>
        <br>
        <a href="index.html" class="nav-link">← Return to Veritas Master Hub</a>
    </div>
</body>
</html>
