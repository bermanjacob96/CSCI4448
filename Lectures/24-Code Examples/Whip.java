public class Whip extends CondimentDecorator {

  public Whip(Beverage beverage) {
    super(beverage, "Whip");
  }

  public double cost() {
    return .10 + getBeverage().cost();
  }

}
