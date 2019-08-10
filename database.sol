pragma solidity ^0.5.10;

contract database {
    struct object {
        //atributes
        int id;
        int number;
        string text;
        bool is_deleted; //default = false
    }

    int id = 0;
    mapping (int => int) list;

    //methods
    function auto_increment() public {
        id = id + 1;
    }

}