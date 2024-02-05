<html np-app="">
  <head>
    <title>My AngularJS App</title>
    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.5.6/angular.min.js"></script>
  </head>
  <body>
        <input type="text" name="name1" ng-model="x"></input>
        <p np-bind="x">
            This is My Name:-
        </p>
  </body >
</html>