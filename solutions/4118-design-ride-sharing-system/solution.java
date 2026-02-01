class RideSharingSystem {
    LinkedHashSet<Integer>rider;
    LinkedHashSet<Integer>driver;
    public RideSharingSystem() {
        rider=new LinkedHashSet<>();
        driver=new LinkedHashSet<>();
    }
    
    public void addRider(int riderId) {
        rider.add(riderId);
    }
    
    public void addDriver(int driverId) {
        driver.add(driverId);
    }
    
    public int[] matchDriverWithRider() {
        if(rider.isEmpty() || driver.isEmpty())
            return new int[]{-1,-1};
        Iterator<Integer>riderIt=rider.iterator();
        Iterator<Integer>driverIt=driver.iterator();
        int rId=riderIt.next();
        int dId=driverIt.next();
        rider.remove(rId);
        driver.remove(dId);
        return new int[]{dId,rId};
    }
    
    public void cancelRider(int riderId) {
        rider.remove(riderId);
    }
}

/**
 * Your RideSharingSystem object will be instantiated and called as such:
 * RideSharingSystem obj = new RideSharingSystem();
 * obj.addRider(riderId);
 * obj.addDriver(driverId);
 * int[] param_3 = obj.matchDriverWithRider();
 * obj.cancelRider(riderId);
 */
