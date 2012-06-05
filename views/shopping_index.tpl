%rebase layout title="Shopping Lists"
<table class="table">
  <thead>
    <tr>
      <th> Date </th>
      <th> Items Bought </th>
      <th> Cost </th>
      <th> </th>
    </tr>
  </thead>
  <tbody>
%for list in lists:
%  x = list.shopping
    <tr>
      <td>{{ time_to_string(x["date"]) }}</td>
      <td>
        {{ ", ".join([ i["name"] for i in x["ingredients"] ]) }}
      </td>
      <td>{{ "$%.2f" % list.cost }}</td>
      <td><a href="/shopping/{{x["_id"]}}">Details</a></td>
    </tr>
%end
  </tbody>
</table>



