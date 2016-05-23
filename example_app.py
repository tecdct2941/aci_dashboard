from example_samplers import *
from apic import ApicTemp, ApicHealth, TenantHealth, NetworkEndpointsCount, EpgStats, EpgStatsFake, FabricMembersHealth, EpgEndPointsFake, AllTenants

def run(app, xyzzy):
    samplers = [
        SynergySampler(xyzzy, 3),
        BuzzwordsSampler(xyzzy, 2),
        ConvergenceSampler(xyzzy, 1),
        ApicTemp(xyzzy,5),
        ApicHealth(xyzzy,5),
        TenantHealth(app=xyzzy, interval=5, tenant = 'L2-Test'),
        TenantHealth(app=xyzzy, interval=5, tenant='infra'),
        NetworkEndpointsCount(app=xyzzy, interval=5, tenant='L2-Test', anp='L2-Test', epg='VLAN96', netmax=254),
        EpgStats(app=xyzzy, interval=30, tenant='L2-Test', anp='L2-Test', epg='VLAN96'),
        FabricMembersHealth(app=xyzzy, interval=10 ),
        EpgStatsFake(xyzzy,5),
        EpgEndPointsFake(xyzzy, 10),
        AllTenants(xyzzy, 10)
    ]

    try:
        app.run(debug=True,
                port=5000,
                threaded=True,
                use_reloader=False,
                use_debugger=True
                )
    finally:
        print "Disconnecting clients"
        xyzzy.stopped = True
        
        print "Stopping %d timers" % len(samplers)
        for (i, sampler) in enumerate(samplers):
            sampler.stop()

    print "Done"
