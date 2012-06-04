<h1>Enter New Shopping List</h1>
Enter the items bought at the store.  Enter each item bough along with the unit (can, box, or if it's a single item enter "item").  Include the quantity and the price.
<form action="/shopping" method="post">
  <table>
    <tr>
      <th>Name</th>
      <th>Unit</th>
      <th>Quantity</th>
      <th>Price</th>
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
      <td>
        <input type="text" name="ingredient[{{i}}][price]" />
      </td>
    </tr>
%end
  </table>
  <input type="submit"/>
</form>
