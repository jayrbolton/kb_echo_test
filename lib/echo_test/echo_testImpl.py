# -*- coding: utf-8 -*-
#BEGIN_HEADER
import os
from KBaseReport.KBaseReportClient import KBaseReport
#END_HEADER


class echo_test:
    '''
    Module Name:
    echo_test

    Module Description:
    A KBase module: echo_test
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = "4b5a37e6fed857c199df65191ba3344a467b8aab"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        #END_CONSTRUCTOR
        pass


    def echo(self, ctx, params):
        """
        :param params: instance of type "Params" -> structure: parameter
           "message" of String, parameter "workspace_name" of String
        :returns: instance of type "Results" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String,
           parameter "message" of String
        """
        # ctx is the context object
        # return variables are: results
        #BEGIN echo
        ws_name = params['workspace_name']
        report_client = KBaseReport(self.callback_url)
        report = report_client.create_extended_report({
            'message': params.get('message', ''),
            'workspace_name': ws_name,
            'report_object_name': 'echo_response'
        })
        results = {
            'report_name': report['name'],
            'report_ref': report['ref'],
            'message': params.get('message', '')
        }
        #END echo

        # At some point might do deeper type checking...
        if not isinstance(results, dict):
            raise ValueError('Method echo return value ' +
                             'results is not type dict as required.')
        # return the results
        return [results]

    def echo_fail(self, ctx, params):
        """
        Function that always throws an exception for testing job failures
        :param params: instance of type "Params" -> structure: parameter
           "message" of String, parameter "workspace_name" of String
        :returns: instance of type "Results" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String,
           parameter "message" of String
        """
        # ctx is the context object
        # return variables are: results
        #BEGIN echo_fail
        results = {}
        raise ValueError()
        #END echo_fail

        # At some point might do deeper type checking...
        if not isinstance(results, dict):
            raise ValueError('Method echo_fail return value ' +
                             'results is not type dict as required.')
        # return the results
        return [results]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
