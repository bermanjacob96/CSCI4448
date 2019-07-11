public class Milk extends CondimentDecorator {

  public Milk(Beverage beverage) {
    super(beverage, "Milk");
  }

  public double cost() {
    return .10 + getBeverage().cost();
  }

}
