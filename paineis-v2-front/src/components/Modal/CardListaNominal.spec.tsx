import { parseDate } from "./CardListaNominal";
import moment from "moment";

jest.mock("moment", () => {
  const originalMoment = jest.requireActual("moment");
  const mockedMoment = function (args: any) {
    return originalMoment(args);
  };
  mockedMoment.utc = jest.fn((args) => originalMoment.utc(args));
  return mockedMoment;
});

describe("parseDate", () => {
  it("should handle valid dates", () => {
    expect(parseDate("2023-12-01")).toBe("01/12/2023");
  });

  it("should handle invalid dates containing 'Invalid'", () => {
    // When moment returns an invalid date string, parseDate should fallback to str.split("-").reverse().join("/")
    // Pass an invalid date format that moment can't parse
    // Normally it returns 'Invalid date', which hits the indexOf('Invalid') != -1 branch
    expect(parseDate("invalid-date")).toBe("date/invalid");
  });

  it("should handle empty string", () => {
    expect(parseDate("")).toBe("");
  });

  it("should handle error in moment.utc", () => {
    // Force moment.utc to throw an error
    (moment.utc as jest.Mock).mockImplementationOnce(() => {
      throw new Error("Simulated error");
    });

    // Test that the fallback logic is executed correctly in the catch block
    // The fallback logic is: return str.split('-').reverse().join('/')
    expect(parseDate("2023-12-01")).toBe("01/12/2023");
  });
});
