def main():
    """
    This function is the entry point of the application. It initializes the NetflowTracker,
    tracks netflows, and saves the results to a JSON file.

    Parameters:
    None

    Returns:
    None
    """
    tracker = NetflowTracker()
    netflows = tracker.track_netflows()
    tracker.save_to_json(netflows)
    
if __name__ == "__main__":
    main()