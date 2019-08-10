pragma solidity ^0.5.10;

contract database {
    struct Object {
        //atributes
        int number;
        string text;
        bool is_deleted; //default = false
    }

    int id = 0;
    mapping (int => Object) list;

    //each id is unique
    function auto_increment() internal {
        id++;
    }

    //setters
    function set_number(int idd, int x) internal {
        if (!list[idd].is_deleted) {
            list[idd].number = x;
        }
    }

    function set_text(int idd, string memory x) internal {
        if (!list[idd].is_deleted) {
            list[idd].text = x;
        }
    }

    function deleted(int idd) internal {
        list[idd].is_deleted = true;
    }

    //getters
    function get_number(int idd) public view returns (int) {
        if (!list[idd].is_deleted) {
            return list[idd].number;
        } else {
            return 0;
        }
    }

    function get_text(int idd) public view returns (string memory) {
        if (!list[idd].is_deleted) {
            return list[idd].text;
        } else {
            return "";
        }
    }

    //create - append
    function create(int n, string memory t) public {
        list[id] = Object({
            number: n,
            text: t,
            is_deleted: false
        });
        auto_increment();
    }
}