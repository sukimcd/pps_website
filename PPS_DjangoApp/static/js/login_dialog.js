<script src="https://code.jquery.com/jquery-1.12.4.js"></script>
<script src="https://code.jquery.com/ui/1.12.0/jquery-ui.js"></script>
  <script>
    
document.getElementById("Login").addEventListener("click", function(evt){
    ("#login_dialog" ).dialog();
})

  </script>
  
  <div id="login_dialog" title="Login">
      <form method='POST' action=''>
          {{ login_dialog.as_table }}
          <input type='submit' value="Login"/>
      </form>    
  </div>