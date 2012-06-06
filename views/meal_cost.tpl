%rebase layout title="Meal Cost"

<p>Your total cost is {{ "$%.2f" % cost }}.</p>

<p>Breakdown of costs:</p>
<table class="table">
  <thead>
    <tr>
      <th>Name</th>
      <th>Unit</th>
      <th>Quantity</th>
      <th>Per Unit Cost</th>
      <th>Total Cost</th>
    </tr>
  </thead>
  <tbody>
% for i in ingredients:
    <tr>
      <td>{{ i["name"] }}</td>
      <td>{{ i["unit"] }}</td>
      <td>{{ i["quantity"] }}</td>
      <td>{{ "$%.2f" % i["price"] }}</td>
      <td>{{ "$%.2f" % i["cost"] }}</td>
    </tr>
%end
  </tbody>
</table>

<a class="btn" href="/meals/{{id}}/delete">Delete</a>
