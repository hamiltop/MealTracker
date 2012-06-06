%rebase layout title="Meals"
<table class="table">
  <thead>
    <tr>
      <th> Date </th>
      <th> Ingredients</th>
      <th> Name </th>
      <th> Cost </th>
      <th> </th>
    </tr>
  </thead>
  <tbody>
%for meal in meals:
%  x = meal.meal 
    <tr>
      <td>{{ time_to_string(x["date"]) }}</td>
      <td>
        {{ ", ".join([ i["name"] for i in x["meal"] ]) }}
      </td>
      <td>{{ "$%.2f" % meal.cost }}</td>
      <td><a href="/meals/{{x["_id"]}}">Details</a></td>
    </tr>
%end
  </tbody>
</table>



