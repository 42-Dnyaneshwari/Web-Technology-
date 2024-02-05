let x = angular.module('myModule', []);
x.controller('myController', function($scope) {
    $scope.arr = [{ id: 1, Name: 'abc' }, { id: 2, Name: 'xyz' }, { id: 3, Name: 'pqs' }];

    $scope.AddItem = function() {
        let n = {};
        n.id = $scope.tid;
        n.Name = $scope.tname;
        $scope.arr.push(n);
    }

    $scope.DeleteItem = function(y) {
        $scope.arr = $scope.arr.filter(function(o) {
            return o.id !== y;
        });
    }

    $scope.Update = function(y) {
        let newName = prompt("Enter the new name for the task with ID " + y);
        if (newName !== null) {
            for (let i = 0; i < $scope.arr.length; i++) {
                if ($scope.arr[i].id == y) {
                    $scope.arr[i].Name = newName;
                    break;
                }
            }
        }
    }
});
