#import <Foundation/Foundation.h>
#import "ASPObject.h"

/**
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen
 * Do not edit the class manually.
 */

#import "ASPWorkingTime.h"


@protocol ASPWeekDay
@end

@interface ASPWeekDay : ASPObject


@property(nonatomic) NSString* dayType;

@property(nonatomic) NSNumber* dayWorking;

@property(nonatomic) NSDate* fromDate;

@property(nonatomic) NSDate* toDate;

@property(nonatomic) NSArray<ASPWorkingTime>* workingTimes;

@end
