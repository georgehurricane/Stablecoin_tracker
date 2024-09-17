from src.netflow_tracker import NetflowTracker

def main():
    tracker = NetflowTracker()
    netflows = tracker.track_netflows()
    tracker.save_to_json(netflows)

if __name__ == '__main__':
    main()