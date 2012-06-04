% setdefault("title","Ingredients List")
% print "in template"
%rebase layout title=title
<h2>Average Cost of Ingredients</h2>
This is your personal database of ingredients along with their average price.  It reflects all items that have been entered in shopping lists.

<table class="table">
  <thead>
    <tr>
      <th>Name</th>
      <th>Unit</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
%for x in averages:
    <tr>
      <td>{{x[0][1]}}</td>
      <td>{{x[0][2]}}</td>
%average = "$%.2f" % (float(x[1][0])/x[1][1])
      <td>{{ average }}</td>
    </tr>
%end
  </tbody>
</table>

<h2> Cost of ingredients in individual purchase </h2>
<table class="table">
  <thead>
    <tr>
      <th>Name</th>
      <th>Unit</th>
      <th>Price</th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
%for x in all:
    <tr>
      <td>{{x["name"]}}</td>
      <td>{{x["unit"]}}</td>
      <td>{{ "$%.2f" % x["price"]}}</td>
      <td>{{x["quantity"]}}</td>
    </tr>
%end
  </tbody>
</table>
