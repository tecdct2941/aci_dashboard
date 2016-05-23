
import time
import collections



jsondata={
  "totalCount": "14",
  "imdata": [
    {
      "topSystem": {
        "attributes": {
          "address": "10.9.104.95",
          "childAction": "",
          "configIssues": "",
          "currentTime": "2016-05-01T14:28:06.179-04:00",
          "dn": "topology/pod-1/node-201/sys",
          "fabricId": "1",
          "fabricMAC": "00:22:BD:F8:19:FF",
          "id": "201",
          "inbMgmtAddr": "10.7.60.101",
          "inbMgmtAddr6": "0.0.0.0",
          "lcOwn": "local",
          "modTs": "2016-04-15T14:48:52.120-04:00",
          "mode": "unspecified",
          "monPolDn": "uni/fabric/monfab-default",
          "name": "leaf1",
          "oobMgmtAddr": "0.0.0.0",
          "oobMgmtAddr6": "0.0.0.0",
          "podId": "1",
          "role": "leaf",
          "serial": "SAL1813NZBB",
          "state": "in-service",
          "status": "",
          "systemUpTime": "15:23:21:29.000"
        },
        "children": [
          {
            "healthInst": {
              "attributes": {
                "childAction": "",
                "chng": "8",
                "cur": "78",
                "maxSev": "cleared",
                "prev": "72",
                "rn": "health",
                "status": "",
                "twScore": "78",
                "updTs": "2016-04-27T11:46:47.051-04:00"
              }
            }
          }
        ]
      }
    },
    {
      "topSystem": {
        "attributes": {
          "address": "10.9.96.95",
          "childAction": "",
          "configIssues": "",
          "currentTime": "2016-05-01T14:28:06.179-04:00",
          "dn": "topology/pod-1/node-101/sys",
          "fabricId": "1",
          "fabricMAC": "00:22:BD:F8:19:FF",
          "id": "101",
          "inbMgmtAddr": "10.7.60.98",
          "inbMgmtAddr6": "0.0.0.0",
          "lcOwn": "local",
          "modTs": "2016-04-15T16:33:25.942-04:00",
          "mode": "unspecified",
          "monPolDn": "uni/fabric/monfab-default",
          "name": "spine1",
          "oobMgmtAddr": "0.0.0.0",
          "oobMgmtAddr6": "0.0.0.0",
          "podId": "1",
          "role": "spine",
          "serial": "FGE17520516",
          "state": "in-service",
          "status": "",
          "systemUpTime": "15:21:38:59.000"
        },
        "children": [
          {
            "healthInst": {
              "attributes": {
                "childAction": "",
                "chng": "1",
                "cur": "99",
                "maxSev": "cleared",
                "prev": "98",
                "rn": "health",
                "status": "",
                "twScore": "99",
                "updTs": "2016-04-20T13:22:34.477-04:00"
              }
            }
          }
        ]
      }
    },
    {
      "topSystem": {
        "attributes": {
          "address": "10.9.104.94",
          "childAction": "",
          "configIssues": "",
          "currentTime": "2016-05-01T14:28:06.179-04:00",
          "dn": "topology/pod-1/node-102/sys",
          "fabricId": "1",
          "fabricMAC": "00:22:BD:F8:19:FF",
          "id": "102",
          "inbMgmtAddr": "10.7.60.90",
          "inbMgmtAddr6": "0.0.0.0",
          "lcOwn": "local",
          "modTs": "2016-04-15T16:33:28.870-04:00",
          "mode": "unspecified",
          "monPolDn": "uni/fabric/monfab-default",
          "name": "spine2",
          "oobMgmtAddr": "0.0.0.0",
          "oobMgmtAddr6": "0.0.0.0",
          "podId": "1",
          "role": "spine",
          "serial": "FGE1752056T",
          "state": "in-service",
          "status": "",
          "systemUpTime": "15:21:38:54.000"
        },
        "children": [
          {
            "healthInst": {
              "attributes": {
                "childAction": "",
                "chng": "1",
                "cur": "99",
                "maxSev": "cleared",
                "prev": "98",
                "rn": "health",
                "status": "",
                "twScore": "99",
                "updTs": "2016-04-20T13:22:34.478-04:00"
              }
            }
          }
        ]
      }
    },
    {
      "topSystem": {
        "attributes": {
          "address": "10.9.104.93",
          "childAction": "",
          "configIssues": "",
          "currentTime": "2016-05-01T14:28:06.179-04:00",
          "dn": "topology/pod-1/node-202/sys",
          "fabricId": "1",
          "fabricMAC": "00:22:BD:F8:19:FF",
          "id": "202",
          "inbMgmtAddr": "10.7.60.134",
          "inbMgmtAddr6": "0.0.0.0",
          "lcOwn": "local",
          "modTs": "2016-04-15T14:49:13.382-04:00",
          "mode": "unspecified",
          "monPolDn": "uni/fabric/monfab-default",
          "name": "leaf2",
          "oobMgmtAddr": "0.0.0.0",
          "oobMgmtAddr6": "0.0.0.0",
          "podId": "1",
          "role": "leaf",
          "serial": "SAL1813NZ9F",
          "state": "in-service",
          "status": "",
          "systemUpTime": "15:23:21:13.000"
        },
        "children": [
          {
            "healthInst": {
              "attributes": {
                "childAction": "",
                "chng": "2",
                "cur": "99",
                "maxSev": "cleared",
                "prev": "97",
                "rn": "health",
                "status": "",
                "twScore": "99",
                "updTs": "2016-04-26T11:37:16.900-04:00"
              }
            }
          }
        ]
      }
    },
    {
      "topSystem": {
        "attributes": {
          "address": "10.9.104.91",
          "childAction": "",
          "configIssues": "",
          "currentTime": "2016-05-01T14:28:06.180-04:00",
          "dn": "topology/pod-1/node-204/sys",
          "fabricId": "1",
          "fabricMAC": "00:22:BD:F8:19:FF",
          "id": "204",
          "inbMgmtAddr": "10.7.60.168",
          "inbMgmtAddr6": "0.0.0.0",
          "lcOwn": "local",
          "modTs": "2016-04-15T14:49:13.901-04:00",
          "mode": "unspecified",
          "monPolDn": "uni/fabric/monfab-default",
          "name": "leaf4",
          "oobMgmtAddr": "0.0.0.0",
          "oobMgmtAddr6": "0.0.0.0",
          "podId": "1",
          "role": "leaf",
          "serial": "SAL1813NZ9Q",
          "state": "in-service",
          "status": "",
          "systemUpTime": "15:23:21:06.000"
        },
        "children": [
          {
            "healthInst": {
              "attributes": {
                "childAction": "",
                "chng": "1",
                "cur": "99",
                "maxSev": "cleared",
                "prev": "98",
                "rn": "health",
                "status": "",
                "twScore": "99",
                "updTs": "2016-04-21T09:40:48.252-04:00"
              }
            }
          }
        ]
      }
    },
    {
      "topSystem": {
        "attributes": {
          "address": "10.9.0.1",
          "childAction": "",
          "configIssues": "",
          "currentTime": "2016-05-01T14:28:06.181-04:00",
          "dn": "topology/pod-1/node-1/sys",
          "fabricId": "1",
          "fabricMAC": "00:22:BD:F8:19:FF",
          "id": "1",
          "inbMgmtAddr": "10.7.60.11",
          "inbMgmtAddr6": "0.0.0.0",
          "lcOwn": "local",
          "modTs": "2015-05-20T15:23:35.262-04:00",
          "mode": "unspecified",
          "monPolDn": "uni/fabric/monfab-default",
          "name": "devpod1-apic1a",
          "oobMgmtAddr": "10.122.226.51",
          "oobMgmtAddr6": "0.0.0.0",
          "podId": "1",
          "role": "controller",
          "serial": "FCH1814V0YF",
          "state": "in-service",
          "status": "",
          "systemUpTime": "15:23:50:21.000"
        }
      }
    },
    {
      "topSystem": {
        "attributes": {
          "address": "10.9.96.64",
          "childAction": "",
          "configIssues": "",
          "currentTime": "2016-05-01T14:28:06.179-04:00",
          "dn": "topology/pod-1/node-103/sys",
          "fabricId": "1",
          "fabricMAC": "00:22:BD:F8:19:FF",
          "id": "103",
          "inbMgmtAddr": "10.7.60.97",
          "inbMgmtAddr6": "0.0.0.0",
          "lcOwn": "local",
          "modTs": "2016-04-15T16:33:39.866-04:00",
          "mode": "unspecified",
          "monPolDn": "uni/fabric/monfab-default",
          "name": "spine3",
          "oobMgmtAddr": "0.0.0.0",
          "oobMgmtAddr6": "0.0.0.0",
          "podId": "1",
          "role": "spine",
          "serial": "SAL18474VEN",
          "state": "in-service",
          "status": "",
          "systemUpTime": "15:21:40:51.000"
        },
        "children": [
          {
            "healthInst": {
              "attributes": {
                "childAction": "",
                "chng": "1",
                "cur": "99",
                "maxSev": "cleared",
                "prev": "98",
                "rn": "health",
                "status": "",
                "twScore": "99",
                "updTs": "2016-04-20T13:22:34.550-04:00"
              }
            }
          }
        ]
      }
    },
    {
      "topSystem": {
        "attributes": {
          "address": "10.9.104.92",
          "childAction": "",
          "configIssues": "",
          "currentTime": "2016-05-01T14:28:06.180-04:00",
          "dn": "topology/pod-1/node-203/sys",
          "fabricId": "1",
          "fabricMAC": "00:22:BD:F8:19:FF",
          "id": "203",
          "inbMgmtAddr": "10.7.60.167",
          "inbMgmtAddr6": "0.0.0.0",
          "lcOwn": "local",
          "modTs": "2016-04-15T14:49:25.889-04:00",
          "mode": "unspecified",
          "monPolDn": "uni/fabric/monfab-default",
          "name": "leaf3",
          "oobMgmtAddr": "0.0.0.0",
          "oobMgmtAddr6": "0.0.0.0",
          "podId": "1",
          "role": "leaf",
          "serial": "SAL1813NZBG",
          "state": "in-service",
          "status": "",
          "systemUpTime": "15:23:21:01.000"
        },
        "children": [
          {
            "healthInst": {
              "attributes": {
                "childAction": "",
                "chng": "1",
                "cur": "99",
                "maxSev": "cleared",
                "prev": "98",
                "rn": "health",
                "status": "",
                "twScore": "99",
                "updTs": "2016-04-21T09:40:24.099-04:00"
              }
            }
          }
        ]
      }
    },
    {
      "topSystem": {
        "attributes": {
          "address": "10.9.104.66",
          "childAction": "",
          "configIssues": "",
          "currentTime": "2016-05-01T14:22:47.437-04:00",
          "dn": "topology/pod-1/node-212/sys",
          "fabricId": "1",
          "fabricMAC": "00:22:BD:F8:19:FF",
          "id": "212",
          "inbMgmtAddr": "0.0.0.0",
          "inbMgmtAddr6": "0.0.0.0",
          "lcOwn": "local",
          "modTs": "2016-04-15T15:06:02.793-04:00",
          "mode": "unspecified",
          "monPolDn": "uni/fabric/monfab-default",
          "name": "sf-leaf1",
          "oobMgmtAddr": "0.0.0.0",
          "oobMgmtAddr6": "0.0.0.0",
          "podId": "1",
          "role": "leaf",
          "serial": "SAL1925H044",
          "state": "in-service",
          "status": "",
          "systemUpTime": "15:23:21:13.000"
        },
        "children": [
          {
            "healthInst": {
              "attributes": {
                "childAction": "",
                "chng": "3",
                "cur": "98",
                "maxSev": "cleared",
                "prev": "95",
                "rn": "health",
                "status": "",
                "twScore": "98",
                "updTs": "2016-04-27T11:29:22.374-04:00"
              }
            }
          }
        ]
      }
    },
    {
      "topSystem": {
        "attributes": {
          "address": "10.9.104.65",
          "childAction": "",
          "configIssues": "",
          "currentTime": "2016-05-01T14:20:39.211-04:00",
          "dn": "topology/pod-1/node-211/sys",
          "fabricId": "1",
          "fabricMAC": "00:22:BD:F8:19:FF",
          "id": "211",
          "inbMgmtAddr": "0.0.0.0",
          "inbMgmtAddr6": "0.0.0.0",
          "lcOwn": "local",
          "modTs": "2016-04-15T15:03:48.499-04:00",
          "mode": "unspecified",
          "monPolDn": "uni/fabric/monfab-default",
          "name": "sf-leaf2",
          "oobMgmtAddr": "0.0.0.0",
          "oobMgmtAddr6": "0.0.0.0",
          "podId": "1",
          "role": "leaf",
          "serial": "SAL1924GKJH",
          "state": "in-service",
          "status": "",
          "systemUpTime": "15:23:20:49.000"
        },
        "children": [
          {
            "healthInst": {
              "attributes": {
                "childAction": "",
                "chng": "3",
                "cur": "98",
                "maxSev": "cleared",
                "prev": "95",
                "rn": "health",
                "status": "",
                "twScore": "98",
                "updTs": "2016-04-19T02:56:35.554-04:00"
              }
            }
          }
        ]
      }
    },
    {
      "topSystem": {
        "attributes": {
          "address": "10.9.104.90",
          "childAction": "",
          "configIssues": "",
          "currentTime": "2016-05-01T14:28:06.181-04:00",
          "dn": "topology/pod-1/node-301/sys",
          "fabricId": "1",
          "fabricMAC": "00:22:BD:F8:19:FF",
          "id": "301",
          "inbMgmtAddr": "10.7.60.135",
          "inbMgmtAddr6": "0.0.0.0",
          "lcOwn": "local",
          "modTs": "2016-04-15T14:50:07.573-04:00",
          "mode": "unspecified",
          "monPolDn": "uni/fabric/monfab-default",
          "name": "leaf5",
          "oobMgmtAddr": "0.0.0.0",
          "oobMgmtAddr6": "0.0.0.0",
          "podId": "1",
          "role": "leaf",
          "serial": "SAL1815PZ7F",
          "state": "in-service",
          "status": "",
          "systemUpTime": "15:23:21:22.000"
        },
        "children": [
          {
            "healthInst": {
              "attributes": {
                "childAction": "",
                "chng": "1",
                "cur": "99",
                "maxSev": "cleared",
                "prev": "98",
                "rn": "health",
                "status": "",
                "twScore": "99",
                "updTs": "2016-04-21T09:24:02.619-04:00"
              }
            }
          }
        ]
      }
    },
    {
      "topSystem": {
        "attributes": {
          "address": "10.9.104.89",
          "childAction": "",
          "configIssues": "",
          "currentTime": "2016-05-01T14:28:06.182-04:00",
          "dn": "topology/pod-1/node-302/sys",
          "fabricId": "1",
          "fabricMAC": "00:22:BD:F8:19:FF",
          "id": "302",
          "inbMgmtAddr": "10.7.60.100",
          "inbMgmtAddr6": "0.0.0.0",
          "lcOwn": "local",
          "modTs": "2016-04-15T14:49:49.036-04:00",
          "mode": "unspecified",
          "monPolDn": "uni/fabric/monfab-default",
          "name": "leaf6",
          "oobMgmtAddr": "0.0.0.0",
          "oobMgmtAddr6": "0.0.0.0",
          "podId": "1",
          "role": "leaf",
          "serial": "SAL1815Q3G6",
          "state": "in-service",
          "status": "",
          "systemUpTime": "15:23:20:38.000"
        },
        "children": [
          {
            "healthInst": {
              "attributes": {
                "childAction": "",
                "chng": "2",
                "cur": "99",
                "maxSev": "cleared",
                "prev": "97",
                "rn": "health",
                "status": "",
                "twScore": "99",
                "updTs": "2016-04-21T09:21:34.662-04:00"
              }
            }
          }
        ]
      }
    },
    {
      "topSystem": {
        "attributes": {
          "address": "10.9.0.2",
          "childAction": "",
          "configIssues": "",
          "currentTime": "2016-05-01T14:28:06.222-04:00",
          "dn": "topology/pod-1/node-2/sys",
          "fabricId": "1",
          "fabricMAC": "00:22:BD:F8:19:FF",
          "id": "2",
          "inbMgmtAddr": "10.7.60.12",
          "inbMgmtAddr6": "0.0.0.0",
          "lcOwn": "local",
          "modTs": "2015-05-20T15:23:35.314-04:00",
          "mode": "unspecified",
          "monPolDn": "uni/fabric/monfab-default",
          "name": "devpod1-apic1b",
          "oobMgmtAddr": "10.122.226.52",
          "oobMgmtAddr6": "0.0.0.0",
          "podId": "1",
          "role": "controller",
          "serial": "FCH1814V0XD",
          "state": "in-service",
          "status": "",
          "systemUpTime": "15:23:42:17.000"
        }
      }
    },
    {
      "topSystem": {
        "attributes": {
          "address": "10.9.0.3",
          "childAction": "",
          "configIssues": "",
          "currentTime": "2016-05-01T14:28:06.222-04:00",
          "dn": "topology/pod-1/node-3/sys",
          "fabricId": "1",
          "fabricMAC": "00:22:BD:F8:19:FF",
          "id": "3",
          "inbMgmtAddr": "10.7.60.14",
          "inbMgmtAddr6": "0.0.0.0",
          "lcOwn": "local",
          "modTs": "2015-05-20T15:23:35.331-04:00",
          "mode": "unspecified",
          "monPolDn": "uni/fabric/monfab-default",
          "name": "devpod1-apic1c",
          "oobMgmtAddr": "10.122.226.53",
          "oobMgmtAddr6": "0.0.0.0",
          "podId": "1",
          "role": "controller",
          "serial": "FCH1814V02Z",
          "state": "in-service",
          "status": "",
          "systemUpTime": "15:23:35:30.000"
        }
      }
    }
  ]
}

items=[]

for topSystem in jsondata['imdata']:
    if (topSystem['topSystem']['attributes']['role'] == "leaf") or (topSystem['topSystem']['attributes']['role'] == "spine"):
        print topSystem['topSystem']['attributes']['role']
        label_string = "%s %s" % (topSystem['topSystem']['attributes']['role'], topSystem['topSystem']['attributes']['id'])
        value_string = "%s" % topSystem['topSystem']['children'][0]['healthInst']['attributes']['cur']

        items.append({'label': label_string, 'value': value_string})


print items






"""
            items=[{'label':'15 Minute Average','value':avg_health},
                   {'label':'Minimum Health','value':min_health},
                   {'label':'Maximum Health','value':max_health}
                   ]
"""