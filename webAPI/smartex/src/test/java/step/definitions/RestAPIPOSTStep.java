package step.definitions;

import io.cucumber.java.Before;
import io.cucumber.java.Scenario;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.restassured.RestAssured;
import io.restassured.response.Response;
import io.restassured.specification.RequestSpecification;
import org.json.JSONArray;
import org.json.JSONObject;
import org.json.JSONString;
import org.junit.Assert;

import java.net.URI;
import java.net.URISyntaxException;

public class RestAPIPOSTStep {

    private final String BASE_URL = "http://localhost:3000/";
    private Response response;
    private Scenario scenario;

    @Before
    public void before(Scenario scenario){
        this.scenario = scenario;
    }

    @Given("Get call to {string}")
    public void getCallToUrl(String url) throws URISyntaxException {
        RestAssured.baseURI = BASE_URL;
        RequestSpecification requestSpecification = RestAssured.given();
        response = requestSpecification.when().get(new URI(url));
    }

    @Then("Response is {string}")
    public void responseIsStatusCode(String statusCode) {
        int actualResponseCode = response.then().extract().statusCode();
        Assert.assertEquals(statusCode, actualResponseCode+"");

    }
}
