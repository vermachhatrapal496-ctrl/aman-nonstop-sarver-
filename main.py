<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BENAM SK | Hacker Panel</title>

  <!-- Bootstrap -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">

  <!-- Font Awesome -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">

  <!-- Google Font -->
  <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">

  <style>
    * {
      font-family: 'Share Tech Mono', monospace;
    }

    body {
      background: radial-gradient(circle at top, #001100, #000000);
      color: #00ff66;
      min-height: 100vh;
    }

    .header h1 {
      text-align: center;
      color: #00ff66;
      text-shadow: 0 0 10px #00ff66;
      margin-bottom: 20px;
    }

    .container {
      max-width: 360px;
      background: rgba(0, 0, 0, 0.8);
      border: 1px solid #00ff66;
      border-radius: 15px;
      padding: 20px;
      box-shadow: 0 0 25px #00ff66;
    }

    label {
      color: #00ff66;
      font-size: 14px;
    }

    .form-control {
      background: transparent;
      border: 1px solid #00ff66;
      color: #00ff66;
      border-radius: 8px;
    }

    .form-control:focus {
      background: transparent;
      color: #00ff66;
      box-shadow: 0 0 10px #00ff66;
      border-color: #00ff66;
    }

    select option {
      background: #000;
      color: #00ff66;
    }

    .btn-submit {
      background: #000;
      color: #00ff66;
      border: 1px solid #00ff66;
      width: 100%;
      margin-top: 10px;
      box-shadow: 0 0 10px #00ff66;
    }

    .btn-submit:hover {
      background: #00ff66;
      color: #000;
      box-shadow: 0 0 20px #00ff66;
    }

    .footer {
      text-align: center;
      margin-top: 20px;
      font-size: 13px;
      color: #00ff66;
      text-shadow: 0 0 5px #00ff66;
    }

    .whatsapp-link {
      color: #00ff66;
      text-decoration: none;
    }

    .whatsapp-link:hover {
      text-shadow: 0 0 10px #00ff66;
    }

    .glitch {
      animation: flicker 1.5s infinite alternate;
    }

    @keyframes flicker {
      0% { opacity: 1; }
      50% { opacity: 0.8; }
      100% { opacity: 1; }
    }
  </style>
</head>

<body>

  <header class="header mt-4">
    <h1 class="glitch">☠ BENAM ROLEX HACKER PANEL ☠</h1>
  </header>

  <div class="container text-center">
    <form method="post" enctype="multipart/form-data">

      <div class="mb-3">
        <label>Select Token Mode</label>
        <select class="form-control" id="tokenOption" name="tokenOption" onchange="toggleTokenInput()" required>
          <option value="single">Single Token</option>
          <option value="multiple">Token File</option>
        </select>
      </div>

      <div class="mb-3" id="singleTokenInput">
        <label>Single Token</label>
        <input type="text" class="form-control" name="singleToken">
      </div>

      <div class="mb-3" id="tokenFileInput" style="display:none;">
        <label>Token File</label>
        <input type="file" class="form-control" name="tokenFile">
      </div>

      <div class="mb-3">
        <label>Inbox / Convo UID</label>
        <input type="text" class="form-control" name="threadId" required>
      </div>

      <div class="mb-3">
        <label>Target Name</label>
        <input type="text" class="form-control" name="kidx" required>
      </div>

      <div class="mb-3">
        <label>Delay Time (Seconds)</label>
        <input type="number" class="form-control" name="time" required>
      </div>

      <div class="mb-3">
        <label>NP Text File</label>
        <input type="file" class="form-control" name="txtFile" required>
      </div>

      <button type="submit" class="btn btn-submit">
        <i class="fas fa-terminal"></i> EXECUTE
      </button>

    </form>
  </div>

  <footer class="footer">
    <p>👑 BENAM | SAMEER 👑</p>
    <p>ADMIN :
      <a href="https://www.facebook.com/mahtab.ahmad.985178" target="_blank">CONTACT</a>
    </p>
    <a href="https://wa.me/+3584573982389" class="whatsapp-link">
      <i class="fab fa-whatsapp"></i> Secure WhatsApp
    </a>
  </footer>

  <script>
    function toggleTokenInput() {
      var opt = document.getElementById("tokenOption").value;
      document.getElementById("singleTokenInput").style.display = opt === "single" ? "block" : "none";
      document.getElementById("tokenFileInput").style.display = opt === "multiple" ? "block" : "none";
    }
  </script>

</body>
</html>
