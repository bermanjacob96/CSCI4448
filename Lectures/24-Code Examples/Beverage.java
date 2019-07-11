public abstract class Beverage {

  private String description = "Unknown Beverage";

  public Beverage(String description) {
    this.description = description;
  }

  public abstract double cost();

  public String getDescription() {
    return description;
  }

}
