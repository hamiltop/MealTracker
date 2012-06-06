%rebase layout title="New  Meal!"

<h2>Ingredients</h2>
<p>A meal must use ingredients and corresponding units already entered in one or more shopping lists.  If the ingredients you are using are not available in the dropdown, you can either enter them in a new shopping list or leave them out of the calculation.</p>
<form class="" action="/meals" method="post">
  <table class="table">
    <tr>
      <th>Name</th>
      <th>Unit</th>
      <th>Quantity</th>
    </tr>
%for i in range(10):
    <tr>
      <td>
        <select name="ingredient[{{i}}][name]" >
%for x in names:
          <option value="{{x}}">{{x}}</option>
%end
        </select>
      </td>
      <td>
        <select name="ingredient[{{i}}][unit]" >
%for x in units:
          <option value="{{x}}">{{x}}</option>
%end
        </select>
      </td>
      <td>
        <input class="input-small" type="text" name="ingredient[{{i}}][quantity]" />
      </td>
    </tr>
%end
  </table>
  <input type="submit"/>
</form>
