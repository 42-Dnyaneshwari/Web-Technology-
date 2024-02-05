let x=angular.module('myModule',[]);
x.controller('myController',function($scope)
{
    $scope.arr=[{id:1,Name:'abc'},{id:2,Name:'xyz'},{id:3,Name:'pqr'}];

    $scope.AddItem=function()
    {
        let n={};
        n.id=$scope.tid;
        n.Name=$scope.tname;
        $scope.arr.push(n)
    }

    $scope.Delete=function(y)
    {
        $scope.arr=$scope.arr.filter(function(o)
        {
            return o.id!=null;
        });
    }

    $scope.Update=funtion(y)
    {
        let nn=prompt("enter the new name for ID ",y);
        if(nn!==null)
        {
            for(let i=0;i<$scope.arr.lenght;i++)
            {
                if($scope.arr[i].id==y)
                {
                    $scope.arr[i].Name=$scope.nn;
                    break;
                }
            }
    }
    }




});