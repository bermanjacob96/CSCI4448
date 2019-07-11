public abstract class CondimentDecorator extends Beverage {

  private Beverage beverage;
  private String   condiment;

  public CondimentDecorator(Beverage beverage, String condiment) {
    super(condiment);
    this.beverage  = beverage;
    this.condiment = condiment;
  }

  protected Beverage getBeverage() {
    return beverage;
  }

  public String getDescription() {
    return getBeverage().getDescription() + ", " + condiment;
  }
}
