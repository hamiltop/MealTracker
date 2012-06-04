<h1>New Meal!</h1>
<h2>Ingredients</h2>
<form action="/meals/cost" method="post">
  <table>
    <tr>
      <th>Name</th>
      <th>Unit</th>
      <th>Quantity</th>
    </tr>
%for i in range(10):
    <tr>
      <td>
        <input type="text" name="ingredient[{{i}}][name]" />
      </td>
      <td>
        <input type="text" name="ingredient[{{i}}][unit]" />
      </td>
      <td>
        <input type="text" name="ingredient[{{i}}][quantity]" />
      </td>
    </tr>
%end
  </table>
  <input type="submit"/>
</form>
