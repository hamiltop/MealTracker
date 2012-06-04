% setdefault("user",current_user())
<html>
<head>
  <link rel="stylesheet" type="text/css/" href="{{ get_url('static', path='style.css') }}" />
  <link rel="stylesheet" type="text/css/" href="{{ get_url('bootstrap', path='css/bootstrap.css') }}" />
  <script src="//ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js" type="text/javascript"></script>
  <script src="{{ get_url('bootstrap', path='js/bootstrap.js') }}"></script>
  <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->  
  <!--[if lt IE 9]>  
  <script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script>  
  <![endif]-->  
</head>
<body>

%include header user=user


<div class="container">
%if defined("title"):
  <h1>{{title}}</h1>
%end

% flash_dict = flash()
%if "error" in flash_dict:
  <div class="alert alert-error">
    <button class="close" data-dismiss="alert">×</button>
    {{ flash_dict["error"] }}  
  </div>
%end
%if "info" in flash_dict:
  <div class="alert alert-info">
    <button class="close" data-dismiss="alert">×</button>
    {{ flash_dict["info"] }}  
  </div>
%end
%if "success" in flash_dict:
  <div class="alert alert-success">
    <button class="close" data-dismiss="alert">×</button>
    {{ flash_dict["success"] }}  
  </div>
%end
<div class="content">
%include
</div>

%include footer
</div>

</body>
</html>
