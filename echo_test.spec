/*
A KBase module: echo_test
*/

module echo_test {

    typedef structure {
        string message;
        string workspace_name;
    } Params;

    typedef structure {
        string report_name;
        string report_ref;
        string message;
    } Results;

    funcdef echo(Params params) returns (Results results) authentication required;

    /* Function that always throws an exception for testing job failures */
    funcdef echo_fail(Params params) returns (Results results) authentication required;
};
