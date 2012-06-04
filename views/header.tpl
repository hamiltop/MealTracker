
<div class="container">
    <div class="navbar navbar-fixed-top">
      <div class="navbar-inner">
        <div class="pull-left">
          <ul class="nav">
            <li><a href="/">Home</a></li>
            <li><a href="/ingredients">My Ingredients</a></li>
            <li><a href="/meals">My Meals</a></li>
          <ul>
        </div>
      <div class="pull-right login"> 
%if user != None:
      Signed in as {{user.user.username}}! <a class="header_link" href="{{ get_url('logout') }}"> Sign out </a>
%else:
      %include login_form 
%end
      </div>
      </div>
    </div>
</div>
  <div class="modal hide" id="createAccount">
    <form action="/users" method="post">
    <div class="modal-header">
      <button type="button" class="close" data-dismiss="modal">×</button>
      <h3>Create a User</h3>
    </div>
    <div class="modal-body">
      Username: <input name="username" type="text" /> <br />
      Password: <input name="password" type="password" />
    </div>
    <div class="modal-footer">
      <button type="button" class="btn" data-dismiss="modal">Cancel</button>
      <button type="submit" href="#" class="btn button-primary">Create</a>
    </div>
    </form>
  </div>

