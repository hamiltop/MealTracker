%rebase layout title="Shopping List"
Enter the items bought at the store.  Enter each item bough along with the unit (can, box, or if it's a single item enter "item").  Include the quantity and the price.  To remove an item, enter 0 as the quantity.
<form action="/shopping/{{_id}}/update" method="post">
  <table>
    <tr>
      <th>Name</th>
      <th>Unit</th>
      <th>Quantity</th>
      <th>Price</th>
    </tr>
%for i in range(len(ingredients)):
    <tr>
      <td>
        <input type="text" value="{{ingredients[i]["name"]}}" name="ingredient[{{i}}][name]" />
      </td>
      <td>
        <input type="text"  value="{{ingredients[i]["unit"]}}" name="ingredient[{{i}}][unit]" />
      </td>
      <td>
        <input type="text"  value="{{ingredients[i]["quantity"]}}" name="ingredient[{{i}}][quantity]" />
      </td>
      <td>
        <input type="text"  value="{{ingredients[i]["price"]}}" name="ingredient[{{i}}][price]" />
      </td>
    </tr>
%end
%for i in range(len(ingredients),10):
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

