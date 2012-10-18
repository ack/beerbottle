<!DOCTYPE html>
<html>
  <head>
    <title>{{ get('title', '') }}</title>
    <link href="/static/css/bootstrap.min.css" rel="stylesheet">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
      body {
        padding-top: 60px; /* topbar spacing */
      }
    </style>
  </head>
  <body>

    <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </a>
          <a class="brand" href="#">pyty</a>
          <div class="nav-collapse collapse">
            <ul class="nav">
              <li class="active"><a href="#">home</a></li>
              <li><a href="#about">about</a></li>
              <li><a href="#contact">contact</a></li>
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>

    <div class="container">    
      %include
    </div>
    
    <script src="http://code.jquery.com/jquery-latest.js"></script>
    <script src="/static/js/bootstrap.min.js"></script>
  </body>
</html>
