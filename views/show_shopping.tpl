%rebase layout title="View Shopping List"

<h2>Information</h2>
<dl class="dl-horizontal">
  <dt>Date:</dt>
  <dd>{{time_to_string(date)}}</dd>
</dl>

<h2>Ingredients</h2>
<table class="table">
  <thead>
    <tr>
      <th>Name</th>
      <th>Unit</th>
      <th>Price</th>
      <th>Quantity</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
%for i in ingredients:
    <tr>
      <td>{{ i["name"] }}</td>
      <td>{{ i["unit"] }}</td>
      <td>{{ i["price"] }}</td>
      <td>{{ i["quantity"] }}</td>
    </tr>
%end
  </tbody>
</table>
